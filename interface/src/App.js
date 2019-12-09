import React, { useState,useEffect } from 'react';
import logo from './logo.png';
import axios from 'axios';
import './App.css';
import { Input,Result,Radio,Modal } from 'antd';
const { Search } = Input;


function App() {
  const [result,setResult] = useState({});
  const [radio,setRadio] = useState({"value":1});
  const [print,setPrint] = useState();
  const [modal,setModal] = useState();
  const search = e =>{
    let Qtype = "phrase";
    if(radio['value']===2){
      Qtype = "ftq"
    }
    axios.get('http://localhost:5000/query?type='+Qtype+'&text='+e).then(response => {
      setResult(Object.values(response.data[1]))
    })
  }
  const onChange = e => {
    console.log('radio checked', e.target.value);
    setRadio({
      value: e.target.value,
    });
  };

  const showModal = e =>{
    let old = modal
    for(let i=0;i<old.length;i++){
      old[i]=false
    }
    old[e] = true
    // console.log(old);
    setModal(old)
  }

  useEffect(()=>{
    // console.log(modal);
    if(modal !==undefined && result[0]!==undefined)
    {
      setPrint(
        <span>{result.map((item,index) => {
          // showModal(index)
          return <><li onClick={()=>showModal(index)} ><a >{Object.values(item)[2]}</a></li>
          <Modal
            title="Basic Modal"
            visible={modal[index]}
            // onOk={this.handleOk}
            // onCancel={this.handleCancel}
          >
            <p>{Object.values(item)[1]}</p>
          </Modal></>
        })}</span>
    );
  }
  console.log(modal);
  })

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
      let newModal=[]
      for(var i = 0; i < result.length; i++) {
        newModal.push(false);
      }
      setModal(newModal)
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
        
      </div>
    </div>
  );
}

export default App;
