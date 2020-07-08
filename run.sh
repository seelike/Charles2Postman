@echo

echo 删除无用文件
rm File/.DS_Store
echo 拆分charls
python 	Batch2Postman.py
echo 拆分完成，开始转换
node index.js
echo 输出文件outputFile
