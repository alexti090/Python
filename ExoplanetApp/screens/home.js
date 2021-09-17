import * as React from 'react';
import {
    View,
    Text,
    Alert, 
    Flatlist,
    Stylesheet,
    SafeAreaView,
} from 'react-native';
import { ListItem } from 'react-native-elements';
import axios from "axios";


export default class HomeScreen extends React.Component{
  constructor(){
    super();
    this.state = {
      listData : [],
      url: "http://localhost:5000/"
    }
  }
  
  componentDidMount(){
    this.getplanetnames();
  }

  getplanetnames = () => {
    const { url } = this.state;
    axios.get(url).then((response)=>{
      return this.setState({
        listData: response.data.data
      })
      console.log(this.state.listData)
    }).catch((error)=>{
      Alert.alert(error)
    });
  }
  
  render(){
    const {listData} = this.state;
    if (listData.length == 0) {
      return(
        <View>
          <Text>Loading...</Text>
        </View>
      )
    }
    else {
      return(
        <View>
          <SafeAreaView>
            <Text>Data Loaded</Text>
          </SafeAreaView>
        </View>
      )
    }
  }
}