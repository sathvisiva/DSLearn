import string

if __name__ == "__main__":
    #X = [[[0] * 300] * 100] * 100
    #Y = [[1, 0, 0, 0, 0, 0]] * 100
    #X = np.array(X, dtype=np.float32)
    #Y = np.array(Y, dtype=np.float32)
    #nn_model = NN.train(X, Y)
    #testX = np.array([[[0] * 300] * 100] * 1, dtype=np.float32)
    #testY = nn_model.predict(testX)
    #print(testY)
    import re

    a = "Tonight in his SOTU, @BarackObama won't talk about Keystone. He will continue to dissemble about his record and play class warfare."
    sentences = re.split(r"([!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~\s+])", a)
    print(sentences)