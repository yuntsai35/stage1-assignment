function showSidebar(){
  const sidebar = document.querySelector('.sidebar')
  sidebar.style.display='flex'
}
function closeSidebar(){
  const sidebar = document.querySelector('.sidebar')
  sidebar.style.display='none'
}


const url1='https://cwpeng.github.io/test/assignment-3-1'
const url2='https://cwpeng.github.io/test/assignment-3-2'
const promises = [
    fetch(url1).then(response => response.json()), 
    fetch(url2).then(response => response.json())  
];

Promise.all(promises)
    .then(results => {
        const json1 = results[0]; 
        const json2 = results[1];
        
        const snameData = json1.rows;
        const picsData = json2.rows;
        
        const last_combine = [];
        
  
        snameData.forEach(snameItem => { 
            const serial_key = snameItem.serial;

            const pic = picsData.find(picItem => picItem.serial === serial_key);
            const picurl=pic.pics
            
            const combineitem = {
                sname: snameItem.sname,
                serial: serial_key,
                pic: picurl 
            };
            
            last_combine.push(combineitem);
        });

      for(const item of last_combine){ 
          const url = item.pic;
          let finalPicUrl = url;

          if (url) {
              const Jpg = url.indexOf('.jpg');
              
              if (Jpg !== -1 && url.length > Jpg + 4) {
                  finalPicUrl = url.substring(0, Jpg + 4); 
              }
      
              item.pic = "https://www.travel.taipei" + finalPicUrl;

      }};

       const name1=last_combine[0].sname;
       const name2=last_combine[1].sname;
       const name3=last_combine[2].sname;
       const content1Span = document.querySelector('.content1 span');
       const content2Span = document.querySelector('.content2 span');
       const content3Span = document.querySelector('.content3 span');


       if (content1Span) {
            content1Span.textContent = name1; 
        }
        if (content2Span) {
            content2Span.textContent = name2;
        }
        if (content3Span) {
            content3Span.textContent = name3;
        }

          
        const frontphotos = document.querySelectorAll('.frontpic');
        let amount=0;
        for(const frontphoto of frontphotos){
        if (amount<3 && amount<last_combine.length) {
          const name=last_combine[amount];
          
            frontphoto.src = name.pic;
            amount++;}
          }


        const pictureContainer=document.querySelector('.picture');
        while (pictureContainer.firstChild){
          pictureContainer.removeChild(pictureContainer.firstChild);
        }
        const start = 3;
        const end = 13; 
        
        for (let i = start; i < end; i++) {
            const item = last_combine[i];

            const picdiv = document.createElement('div');
            picdiv.className = 'pic';
            
            const imgphoto = document.createElement('img');
            imgphoto.className = 'photo';
            imgphoto.src = item.pic;
            imgphoto.alt = item.sname;
            
            const imgstar = document.createElement('img');
            imgstar.className = 'star';
            imgstar.src = 'star.png';
            imgstar.alt = 'star';
            
            const ptext = document.createElement('p');
            ptext.className = 'text';
            ptext.textContent = item.sname;
            
            picdiv.appendChild(imgphoto);
            picdiv.appendChild(imgstar);
            picdiv.appendChild(ptext);
            
            pictureContainer.appendChild(picdiv);
        }
        
        console.log(last_combine);});