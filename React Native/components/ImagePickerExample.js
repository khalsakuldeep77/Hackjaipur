import React, { useState, useEffect } from "react";
import { Button, Image, View, StyleSheet } from "react-native";
import * as ImagePicker from "expo-image-picker";
import Constants from "expo-constants";
import * as FileSystem from "expo-file-system";

const ImagePickerExample = () => {
  const [image, setImage] = useState(null);

  useEffect(() => {
    (async () => {
      if (Constants.platform.ios) {
        const {
          status,
        } = await ImagePicker.requestCameraRollPermissionsAsync();
        if (status !== "granted") {
          alert("Sorry, we need camera roll permissions to make this work!");
        }
      }
    })();
  }, []);

  const pickImage = async () => {
    let result = await ImagePicker.launchImageLibraryAsync({
      mediaTypes: ImagePicker.MediaTypeOptions.All,
      allowsEditing: true,
      aspect: [4, 3],
      quality: 1,
    });

    console.log(result);

    if (!result.cancelled) {
      setImage(result.uri);
    }
  };

  const _takePhoto = async () => {
    let pickerResult = await ImagePicker.launchCameraAsync({
      allowsEditing: true,
      aspect: [4, 3],
      quality: 1,
    });

    if (!pickerResult.cancelled) {
      setImage(pickerResult.uri);
    }
  };

  // const base64 = await FileSystem.readAsStringAsync(image, { encoding: 'base64' });

  // console.log(base64);

  // const convertImage = () => {
  // const base64 = await FileSystem.readAsStringAsync(image, { encoding: 'base64' });
  // };

  // const predict = () => {
  //   var data = {
  //     "url": base64
  //  }

  //  fetch("https://....", {
  //     method: "POST",
  //     headers: headers,
  //     body:  JSON.stringify(data)
  //  })
  //  .then(function(response){
  //   return response.json();
  //  })
  //  .then(function(data){
  //  console.log(data)
  //  });
  // };

  return (
    <View style={styles.container}>
      {image && <Image source={{ uri: image }} style={styles.image} />}
      <Button title="Pick an image from camera roll" onPress={pickImage} />
      <Button title="Take photo from camera" onPress={_takePhoto} />
      <Button title="Predict" onPress={() => {}} />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: "center",
    justifyContent: "center",
  },
  image: {
    width: 200,
    height: 200,
  },
});

export default ImagePickerExample;
