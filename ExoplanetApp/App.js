import React from 'react';
import { StyleSheet, Text, View } from 'react-native';
import { createAppContainer } from "react-navigation";
import { createStackNavigator } from "react-navigation-stack";
import HomeScreen from './screens/home';
import PlanetScreen from './screens/planet';

export default function App() {
  return (
    <AppContainer />
  );
}

const appStackNavigator = createStackNavigator({
  Home: {
    screen: HomeScreen,
    navigationOptions: {
      headerShown: false
    },
  },
  Details: {
    screen: PlanetScreen,
  }
},
{
  intialRouteName: "Home"
})

const AppContainer = createAppContainer(appStackNavigator)