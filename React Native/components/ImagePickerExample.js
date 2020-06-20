import React, { useState, useEffect } from 'react';
import { Button, Image, View, StyleSheet, Platform } from 'react-native';
import * as ImagePicker from 'expo-image-picker';
import Constants from 'expo-constants';

const ImagePickerExample = () => {
	const [image, setImage] = useState(null);

	useEffect(() => {
		(async () => {
			if (Constants.platform.ios) {
				const { status } = await ImagePicker.requestCameraRollPermissionsAsync();
				if (status !== 'granted') {
					alert('Sorry, we need camera roll permissions to make this work!');
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

	const createFormData = (photo, body) => {
		const data = new FormData();
		console.log(photo);
		data.append('photo', {
			name: photo.fileName,
			type: photo.type,

			uri: Platform.OS === 'android' ? photo.uri : photo.uri.replace('file://', ''),
		});

		Object.keys(body).forEach((key) => {
			data.append(key, body[key]);
		});

		return data;
	};

	handleUploadPhoto = () => {
		fetch('http:192.168.56.1//:3000/api/upload', {
			method: 'POST',
			body: createFormData(image, { userId: '123' }),
		})
			.then((response) => response.json())
			.then((response) => {
				console.log('upload success', response);
				alert('Upload success!');
				setImage(null);
			})
			.catch((error) => {
				console.log('upload error', error);
				alert('Upload failed!');
			});
	};

	return (
		<View style={styles.container}>
			{image && (
				<React.Fragment>
					<Image source={{ uri: image }} style={styles.image} />
					<Button title="upload" onPress={handleUploadPhoto} />
				</React.Fragment>
			)}
			<Button title="Pick an image from camera roll" onPress={pickImage} />
		</View>
	);
};

const styles = StyleSheet.create({
	container: {
		flex: 1,
		alignItems: 'center',
		justifyContent: 'center',
	},
	image: {
		width: 200,
		height: 200,
	},
});

export default ImagePickerExample;
