# How To Run My Project？

## Project Structure

```python
code
│  neighbor_list_recom.pickle
│  __init__.py
│          
└─server
    │  image_vectorizer.py
    │  neighbor_list_recom.pickle
    │  rest-server.py
    │  search.py
    │  
    ├─database
    │  │  favorites.txt
    │  │  
    │  ├─dataset # put your images for training into this folder 
    │  │      
    │  └─tags # put your tags into this folder
    │          
    ├─frontend
    │              
    ├─imagenet # put your classify_image_graph_def.pb into this folder
    │      
    ├─static
    │  ├─images
    │  │      
    │  └─result
    │          
    └─uploads
```

## Front-end

After you have entered the `code/server` folder, please run the command below:

```javascript
cd frontend
yarn install
yarn serve
```

Then you can see the website on `localhost:8080`

if you haven't install yarn yet, you can't open my website by this way. You should first use ``` npm ``` to install yarn.

```python
npm install yarn 
```

then add it to your environment variables.
After installation , you can use the command below to check if yarn is installed successfully.

```python
yarn --version
```

## Back-end

After you have entered the `code/server` folder and installed all dependencies, please run the command below:

```python
# train model
python image_vectorizer.py
# run back-end
python rest-server.py
```

Then the backend will run on ``` localhost:3367 ```.     

If you have any trouble running my project, you can see my "演示视频.mp4" in the folder.

