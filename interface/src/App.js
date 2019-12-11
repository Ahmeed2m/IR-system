import React, { useState,useEffect } from 'react';
import logo from './logo.png';
import axios from 'axios';
import './App.css';
import { Input,Result,Radio,Modal } from 'antd';
var uuid = require('uuid');
const { Search } = Input;


function App() {
  const [result,setResult] = useState({});
  const [radio,setRadio] = useState({"value":1});
  const [print,setPrint] = useState();
  const [modal,setModal] = useState(["NULL",false,"NULL"]);

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

  const handleOk = e => {
    setModal(['',false,''])
  };

  const handleCancel = e => {
    setModal(['',false,''])
  };

  const showModal = item =>{
    let score = " "
    if(item['score']!== undefined){
      score = "score : " + item['score']
    }
    setModal([item['title'],true,item['text'],score,item['src']])
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
