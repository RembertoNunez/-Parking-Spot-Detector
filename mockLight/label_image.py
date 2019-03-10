#Author: Pete Warden
#Modified by: Daniel Ochoa
#last Modified: 05-9-17
#Description: This program takes in an image and scores it based on the previously train file
#Once the image is cored it writes the top score into parkingScores.txt
#Got the code from   https://codelabs.developers.google.com/codelabs/tensorflow-for-poets/#0


import tensorflow as tf, sys

#this thats in the image path and saves it into the variable
image_path = sys.argv[1]

# Read in the image_data
image_data = tf.gfile.FastGFile(image_path, 'rb').read()

# Loads label file, strips off carriage return
label_lines = [line.rstrip() for line 
                   in tf.gfile.GFile("light.txt")]

# Unpersists graph from file
with tf.gfile.FastGFile("light.pb", 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    _ = tf.import_graph_def(graph_def, name='')

with tf.Session() as sess:
    # Feed the image_data as input to the graph and get first prediction
    softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
    
    predictions = sess.run(softmax_tensor, \
             {'DecodeJpeg/contents:0': image_data})
    
    # Sort to show labels of first prediction in order of confidence
    top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
    
    #saves the top store into parkingScore.txt
    score = predictions[0][top_k[0]]
    file = open("parkingScores.txt","a")
    file.write(str(score))
    file.write("\n")
    file.close()
    
    for node_id in top_k:
        human_string = label_lines[node_id]
        score = predictions[0][node_id]
        print('%s (score = %.5f)' % (human_string, score))
