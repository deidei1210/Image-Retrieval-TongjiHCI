<template>
  <el-container>
    <!-- 顶部的bar -->
    <el-header style="height: 60px">
      <div style="display: flex; align-items: center;">
        <i class="el-icon-picture" style="margin-left: 1%;"></i>
        <span style="margin-left: 1%;font-weight: bold">Search what you want!</span>
        <el-menu default-active="/" style="margin-left: 3%;" router mode="horizontal" background-color="#605051"
          text-color="#FCE8E8" active-text-color="#E6E6FA">
          <el-menu-item index="/">
            <i class="el-icon-search" style="margin-right: 8%"></i>
            <span slot="title" style="font-size: medium">图片检索</span>
          </el-menu-item>
          <el-menu-item index="/collect">
            <i class="el-icon-star-off" style="margin-right: 8%"></i>
            <span slot="title" style="font-size: medium">我的收藏</span>
          </el-menu-item>
        </el-menu>
      </div>
    </el-header>
    <el-container>
      <el-container>
        <el-main> <router-view></router-view> </el-main>
        <!-- 底部的边框 -->
        <el-footer style="position:fixed;bottom:0px;width:100%;margin-left: 0px;">Github@deidei1210 2051498储岱泽 大二</el-footer>
      </el-container>
    </el-container>
  </el-container>
</template>
<script>
export default {
  name: "App",
};
</script>
<style scoped>
.el-header,
.el-footer {
  background-color: #605051;
  color: white;
}

.el-icon-picture {
  font-size: 1.5em;
}

.el-footer {
  line-height: 60px;
  text-align: center;
}
</style>
