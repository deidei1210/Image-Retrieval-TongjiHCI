<template>
  <div class="about-page">
    <div v-loading="isCollectionLoading">
      <div
          style="margin: 0 auto"
          class="containerFlex"
          v-if="collectImage.length !== 0"
      >
        <el-row>
          <el-col
              v-for="(item, index) in collectImage.slice(
                (currentPage - 1) * 8,
                currentPage * 8
              )"
              :span="6"
              :key="index"
          >
            <ImageCard
                :disallowedTags="disallowedTags"
                :hideTags="false"
                :imageId="item"
            />
          </el-col>
        </el-row>
        <!--分页符-->
      </div>
    </div>
    <div class="pagination-container">
      <el-pagination
          background
          layout="prev, pager, next"
          :hide-on-single-page="true"
          :page-size="8"
          @current-change="handleCurrentChange"
          :total="collectImage.length"
      >
      </el-pagination>
    </div>
  </div>
</template>
<script>
import ImageCard from "@/components/ImageCard";

export default {
  // eslint-disable-next-line
  name: "Collection",
  components: {
    ImageCard,
  },
  data() {
    return {
      disallowedTags: [],
      collectImage: [],
      collectDialogVisible: false,
      currentPage: 1,
      isSearching: false,
      isCollectionLoading: false,
    };
  },
  methods:{
    handleCurrentChange(val) {
      this.currentPage = val;
    },
    getCollection() {
      this.isCollectionLoading = true;
      this.$axios({
        method: "get",
        url: "/collect/all",
      })
          .then((response) => {
            this.collectImage = response.data;
          })
          .finally(() => {
            this.isCollectionLoading = false;
          });
    },
  },
  mounted() {
    this.getCollection()
  }
};
</script>
<style scoped>
.pagination-container {
  display: flex;
  justify-content: center;
  margin-left: auto;
  margin-right: auto;
}

</style>
