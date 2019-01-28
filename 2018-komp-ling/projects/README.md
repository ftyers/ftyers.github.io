This script will show you an approximate complexity of Finnish text. There are level 1, 2, 3. 
'1' corresponds to basic knowledge reading, '2' is intermediate one and '3' is advanced.

You will need to do the following.
1. Install udpipe http://wiki.apertium.org/wiki/UDPipe (what you need to do is just make udpipe tool callable from your command line (desribed in section "Get the code! ")
2. Locate the file with the text to be analyzed and run the following command 
cat "path_to_analyzed_file"| udpipe --tokenize --tag --parse fin.udpipe > "output_file_name"
(To prevent some hours of training put nob.udpipe file into the location you are going to run this command from (pretrained fin.udpipe is located in udpipe_ready_tools)
Now you have the file ready to be handled by the model
3. Run predict.py and pass parsed file name into it. You will get level prediction to the output
