//task1
function func1(name){ 
  const item = [
    {"point": "悟空",   "x1":0, "y1":0,   "distance": null},
    {"point": "丁滿",   "x1":-1, "y1":4,  "distance": null},
    {"point": "⾟巴",   "x1":-3, "y1":3,  "distance": null},
    {"point": "貝吉塔", "x1":-4, "y1":-1, "distance": null},
    {"point": "特南克斯","x1":1, "y1":-2, "distance": null},
    {"point": "弗利沙", "x1":4, "y1":-1,  "distance": null}]  
  
  let x2,y2;
  for(const i of item){
    if(name==i["point"]){
      x2=i["x1"];
      y2=i["y1"];
    }
  }
  
  for(const t of item){
    t["distance"]=Math.abs(t["x1"]-x2)+ Math.abs(t["y1"]-y2);
  }

  const left=["⾟巴","悟空","特南克斯","貝吉塔"];
  const right=["丁滿","弗利沙"];

  for(const e of item){
    if(left.includes(name)){
      if(right.includes(e["point"])){
        e["distance"]+=2;
      }}else{
        if( left.includes(e["point"])){
          e["distance"]+=2;
        }}}
  
  const dis_list=[]
  for (let m = 0; m < item.length; m++) {
    const d = item[m]["distance"];
    dis_list.push(d)
  }
  let a=null;
  let n=100;
  let num_max=[]
  let num_min=[]
  for(const max of dis_list){
    if(max>0){
      if(max>a){
        a=max;
        num_max=[a]
      }
      if(max<n){
        n=max;
        num_min=[n]
      }}}

  const fit_max=[];
  const fit_min=[];
  for (let f = 0; f < item.length; f++) {
    const d = item[f]["distance"];
    if (d === a){
      fit_max.push(item[f]["point"]);}
    if (d === n){
      fit_min.push(item[f]["point"]);}
  }

  console.log("最遠" + fit_max.join("、") + "；最近" + fit_min.join("、"));
}

func1("⾟巴");  // print 最遠弗利沙；最近丁滿、⾙吉塔
 
func1("悟空");  // print 最遠丁滿、弗利沙；最近特南克斯
 
func1("弗利沙");  // print 最遠⾟巴，最近特南克斯
 
func1("特南克斯");  // print 最遠丁滿，最近悟空

//task2
let reserve=[];
let s1=[];
let s2=[];
let s3=[];

function func2(ss, start, end, criteria){ 
  let c=null;
  let r=null;
  let name=null;

  if(criteria.includes("c")){
    c=criteria.slice(3);
  }else if(criteria.includes("r")){
    r=criteria.slice(3);
  }else if(criteria.includes("name")){
    name = criteria.slice(5);
  }
  let diff_name="";
  if (criteria.includes("name=")){
        diff_name=criteria.slice(5);
        for(const s of ss){
          if(diff_name == s["name"]){
             reserve.push(diff_name);}
        }
        
        const time = [];
        for (let t = start; t <= end; t++) {
          time.push(t);
        }
        if (diff_name === "S1") {
          for (const t of time) {
            if (s1.includes(t)) {        
              console.log("Sorry");
              return;
            }
          }
          s1.push(...time);             
          console.log("S1");
          return;
        } else if (diff_name === "S2") {
          for (const t of time) {
            if (s2.includes(t)) {
              console.log("Sorry");
              return;
            }
          }
          s2.push(...time);
          console.log("S2");
          return;
        } else if (diff_name === "S3") {
          for (const t of time) {
            if (s3.includes(t)) {
              console.log("Sorry");
              return;
            }
          }
          s3.push(...time);
          console.log("S3");
          return;}}

  let possible_list=[];
    if (criteria.includes("c>=")){
        for(const s of ss){
            if(s["c"] >= parseInt(c,10)){
                possible_list.push([s["name"], Math.abs(s["c"] - parseInt(c,10))]);}
    }}else if(criteria.includes("c<=")){
        for(const s of ss)
            if(s["c"] <= parseInt(c,10)){
                possible_list.push([s["name"], Math.abs(s["c"] - parseInt(c,10))]);}}

    if (criteria.includes("r>=")){
        for(const s of ss){
            if(s["r"] >= parseFloat(r)){
                possible_list.push([s["name"], Math.abs(s["r"] - parseFloat(r))]);}
    }}else if(criteria.includes("r<=")){
        for(const s of ss)
            if(s["r"] <= parseFloat(r)){
                possible_list.push([s["name"], Math.abs(s["r"] - parseFloat(r))]);}}

    if (possible_list.length == 0) {
    console.log("Sorry");
    return;
  }

    const time = [];
        for (let t = start; t <= end; t++) {
          time.push(t);
        }

    again:
    while (possible_list.length>0){
        let min_index = 0;
        for (let i = 1; i < possible_list.length; i++) {
          if (possible_list[i][1] < possible_list[min_index][1]) {
            min_index = i;
          }
        }
        diff_name = possible_list[min_index][0];
        possible_list.splice(min_index, 1);

        if (diff_name === "S1") {
          for (const t of time) {
            if (s1.includes(t)) {        
              continue again;
            }
          }
          s1.push(...time);             
          console.log("S1");
          return;
        } else if (diff_name === "S2") {
          for (const t of time) {
            if (s2.includes(t)) {
              continue again;
            }
          }
          s2.push(...time);
          console.log("S2");
          return;
        } else if (diff_name === "S3") {
          for (const t of time) {
            if (s3.includes(t)) {
              continue again;
            }
          }
          s3.push(...time);
          console.log("S3");
          return;}}

    if (possible_list.length == 0) {
      console.log("Sorry");
      return;
  }

    
}


const services=[ 
{"name":"S1", "r":4.5, "c":1000}, 
{"name":"S2", "r":3, "c":1200}, 
{"name":"S3", "r":3.8, "c":800} 
]; 
func2(services, 15, 17, "c>=800");  // S3 
func2(services, 11, 13, "r<=4");  // S3 
func2(services, 10, 12, "name=S3");  // Sorry 
func2(services, 15, 18, "r>=4.5");  // S1 
func2(services, 16, 18, "r>=4");  // Sorry 
func2(services, 13, 17, "name=S1");  // Sorry 
func2(services, 8, 9, "c<=1500");  // S2 
func2(services, 8, 9, "c<=1500");  //S1

//task3
function func3(index){ 
    const q=Math.floor(index / 4);
    const r=index % 4;
    const p=[0,-2,-3,1];
    if (r==0) {
    let x; 
    x=p[0];
    } else if (r==1){
    x=p[1];
    }else if(r==2){
    x=p[1]+p[2];
    }else{
    x=p[1]+p[2]+p[3];
    }
    value= 25 + q *(-2) + x
    console.log(value)
} 
func3(1);  // print 23 
func3(5);  // print 21 
func3(10);  // print 16 
func3(30);  // print 6

//task4
function func4(sp, stat, n){ 
   
  const x= stat.split("")
  let list_index=[];

  for (let s=0; s<x.length; s++){
    if(x[s] == 0){
      list_index.push(s)
     }}
  
  let sp_list=[];
  for(let i of list_index){
    sp_list.push(sp[i]);
  }
  
  let fit_number=[];
  var diff=100;
  for(const p of sp_list){
    if(p>=n){
       const num=Math.abs(n-p);
       if(num<=diff){
        diff=num;
        fit_number=[p];
       }
    }else if(p<n){
      const num=Math.abs(n-p);
      if(num<=diff){
        diff=num;
        fit_number=[p];
      }}}
  const fit_value=fit_number[0];
  const a=sp.indexOf(fit_value);
  console.log(a);

} 
func4([3, 1, 5, 4, 3, 2], "101000", 2);  // print 5 
func4([1, 0, 5, 1, 3], "10100", 4);  // print 4 
func4([4, 6, 5, 8], "1000", 4);  // print 2

