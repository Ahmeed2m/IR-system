import React, { useState,useEffect } from 'react';
import logo from './logo.png';
import axios from 'axios';
import './App.css';
import { Input,Result,Radio,Modal,Button,Alert } from 'antd';
var uuid = require('uuid');
const { Search } = Input;


function App() {
  const [result,setResult] = useState({});
  const [radio,setRadio] = useState({"value":1});
  const [print,setPrint] = useState();
  const [modal,setModal] = useState(["NULL",false,"NULL"]);
  const [setting,setSetting] = useState([false,false]);
  const [loading,setLoading] = useState(false)
  const [error,setError] = useState("")

  const search = e =>{
    let Qtype = "phrase";
    if(radio['value']===2){
      Qtype = "ftq"
    }
    axios.get('http://localhost:7082/query?type='+Qtype+'&text='+e).then(response => {
      setResult(Object.values(response.data))
    })
  }
  const onChange = e => {
    console.log('radio checked', e.target.value);
    setRadio({
      value: e.target.value,
    });
    setPrint("")
  };

  const handleOk = (e,flag=false) => {
    if (flag){
      setSetting([false,false]);
    }else{
      setModal(['',false,'']);
    }
  };

  const handleCancel = (e,flag=false) => {
    if (flag){
      setSetting([false,false]);
    }else{
      setModal(['',false,'']);
    }
  };

  const showModal = item =>{
    let score = " "
    if(item['score']!== undefined){
      score = "score : " + item['score']
    }
    setModal([item['title'],true,item['text'],score,item['src']])
  }
  const showSetting = e => {
    setSetting([true,false])
  }
  const updateIndex = e => {
    setLoading(true)
    axios.get('http://localhost:7082/update')
    .then(response => {
        setLoading(false)
        setError(<Alert message="Success" type="success" showIcon />)
    })
    .catch(e => {
        setError(
          <Alert
            message="Error"
            description="Server Error 500"
            type="error"
            showIcon
          />
        )
    });
  }
  function compare(a, b) {
    const bandA = a.score;
    const bandB = b.score;
    let comparison = 0;
    if (bandA > bandB) {
      comparison = -1;
    } else if (bandA < bandB) {
      comparison = 1;
    }
    return comparison;
  }  
  useEffect(()=>{
    setTimeout(function(){
      setError("")
      setLoading(false)
    }, 2000);
  },[error])
  useEffect(()=>{
    if (result[0] === "500"){
      setPrint(
        <Result
            status="404"
            title="دور تانى كدا"
            subTitle=""
            // extra={<Button type="primary">Back Home</Button>}
        />
      )
    }
    else if (result[0]!==undefined){
      console.log(result);
      let f =result.sort(compare);
      console.log(f);
      setPrint(
        f.map((item) => {
          item['key'] =uuid.v4()
          return <li key={item['key']} onClick={()=>showModal(item)} ><a>{item['title']}</a></li>

        })
      );
    }
  },[result]);

  return (
    <div className="App">
      <div className="topBar">
        <Button type="primary" shape="circle" icon="setting" onClick={showSetting}/>
        <Modal
          title={"Setting"}
          visible={setting[0]}
          footer={[<Button key="submit" type="primary" onClick={e=>{handleOk(e,true)}}>
            Ok
          </Button>]}
          onCancel={e=>{handleCancel(e,true)}}
        >
          <Button type="primary" loading={loading} onClick={updateIndex}>
            Refresh Indexed text
          </Button>
          {error}
        </Modal>
      </div>
      <div className="content">
        <img width="60%" height="20%" src={logo}  alt="logo" />
        <Search
          className="bar"
          placeholder="input search text"
          enterButton="Search"
          size="large"
          onSearch={value => search(value)}
        />
        <Radio.Group onChange={onChange} value={radio['value']}>
        <Radio value={1}>Phrase</Radio>
        <Radio value={2}>Free Text</Radio>
      </Radio.Group>
        
        {print}
        <Modal
          title={modal[0]}
          visible={modal[1]}
          onOk={handleOk}
          onCancel={handleCancel}
          footer={null}
        >
          <p>{modal[2]}</p>
          <footer>{modal[3]}</footer>
          <footer>src: <a target="_blank" href={modal[4]}>Here</a></footer>
        </Modal>
        
      </div>
    </div>
  );
}

export default App;
