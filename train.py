from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import ShortTermFeatures
from pyAudioAnalysis import audioTrainTest as aT

audio_dir = "./GTZAN/genres/"

# Train the model (using SVM as an example)
dirs = ['GTZAN/genres/blues', 'GTZAN/genres/classical', 'GTZAN/genres/country', 'GTZAN/genres/disco', 'GTZAN/genres/hiphop', 'GTZAN/genres/jazz', 'GTZAN/genres/metal', 'GTZAN/genres/pop', 'GTZAN/genres/reggae', 'GTZAN/genres/rock']
aT.extract_features_and_train(dirs, 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "svm", "g_emotion_model", False)

result, P, classNames = aT.file_classification("as-it-was.wav", "g_emotion_model", "svm")
print(f"Predicted Genre: {classNames[int(result)][13:]}")