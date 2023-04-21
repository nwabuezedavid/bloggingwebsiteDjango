const play_btn  = document.querySelectorAll('.play')
const video_con  = document.querySelectorAll('.videoPost')
const slide_center_div_text  = document.querySelectorAll('.hideSlidtext')
const slide_center_div_img  = document.querySelectorAll('.hideSlid')
const leftconbtn  = document.querySelector('.left-con')
const rghtconbtn  = document.querySelector('.rght-con')
const imgCon  = document.querySelector('.slicActiobn')
const bar_click = document.querySelector('.bar__top')
const bar_con  = document.querySelector('.hids__nav')

bar_click.addEventListener('click',()=>{
    bar_con.classList.toggle('hids__nav__show')
    // if (bar_con.classList ='hids__nav__show') {
           
    //     } else {
            
    //         bar_con.classList.add('hids__nav__show')
    //    }
})










var initalCount = 0
leftconbtn.addEventListener('click',()=>{
    slid()
    clearInterval(clearibnter)

})
rghtconbtn.addEventListener('click',()=>{
    slidRighr()
    clearInterval(clearibnter)
})


function slidRighr() {
    initalCount++
    console.log(initalCount);
    imgCon.style.display ='flex-reverse'
    slide_center_div_text.forEach((ec, vals)=>{
    slide_center_div_img.forEach((e, val)=>{
       
if (vals == initalCount ){
    ec.classList.add('showSlidtext')
    
    
} 
else{
    ec.classList.remove('showSlidtext')
    

}
if (val == initalCount ){
    e.classList.add('showSlid')
    
    
} else if(initalCount == slide_center_div_img.length){
    e.classList.add('showSlid')
    initalCount = 0

    
}
// else if(initalCount >= slide_center_div_img.length){
//     e.classList.add('showSlid')
//     initalCount = Number(slide_center_div_img.length)
// }
else{
    e.classList.remove('showSlid')
    

}
    })
    })
   
}



function slid() {
    initalCount++
    slide_center_div_text.forEach((ec, vals)=>{
    slide_center_div_img.forEach((e, val)=>{
       
if (vals == initalCount ){
    ec.classList.add('showSlidtext')
    
    
} 
else{
    ec.classList.remove('showSlidtext')
    

}
if (val == initalCount ){
    e.classList.add('showSlid')
    
    
} else if(initalCount == slide_center_div_img.length){
    e.classList.add('showSlid')
    initalCount = 0
}
else{
    e.classList.remove('showSlid')
    

}
    })
    })
}
 let clearibnter = setInterval(() => {
    
    slid()
}, 5000);


let playMode = true
video_con.audio
play_btn.forEach((e,val) => {
video_con.forEach((es, vald) => {
    if (val == vald) {
        e.addEventListener('click',()=>{
            e.classList.toggle('bi-pause-fill')
            e.classList.toggle('bi-play-fill')
            if(playMode == true){
                es.play()
                playMode = false
            }else{
                es.pause()
                playMode = true
            }
        })
    } 
});
});









// api
// const rghtconbtn  = document.querySelector('.rght-con')
let information_list  = document.querySelector('.sec-left-main-one')
let information_list_adver  = document.querySelectorAll('.recent__container')
let Sone_Sport  = document.querySelector('.sec-left-main-one_Sport')
let url = 'http://127.0.0.1:8000'
let item = ""
let ItemimageArr = []
let sportItem = ""


  
// console.log();

function fetchApi() {
    fetch(url,{
        'method':'GET',
        // 'content-type':'application/json'
    })
    .then(res => res.json())
    .then(data => {
        data.forEach(e => {
            if (e.categories == "tw") {
            
                

            item += `
            <div class="information" >
           
            <a href="" class="main-infor">
            <img src="${url + String(e.files)  }" alt="" class='imgs' >
            <span>
                <h4>${e.title} </h4>
                <b>

                    <strong>(${e.viewCount})views</strong>
                    <small>${e.created}</small>
                  </b>
            </span>
            </a >
            </div>

            `
            information_list.innerHTML = item
               let imageConsa = information_list.querySelector('.main-infor')
                // let mams = imageConsa.querySelector('.imgs')
                console.log(imageConsa);
                // imageConsa.forEach(e => {
                    //     console.log(item);
                
                    // });

        } 
            else if (e.categories == "sp") {
             
                sportItem += `
            <div class="information" >
           
            <a href="" class="main-infor">
           
            <img src="${url + String(e.files)  }" alt="" class='imgs_dport' >
            <span>
                <h4>${e.title} </h4>
                <b>

                    <strong>(${e.viewCount})views</strong>
                    <small>${e.created}</small>
                  </b>
            </span>
            </a >
            </div>

            `
            Sone_Sport.innerHTML = sportItem
        }

        
    
        });
    })
}

fetchApi()
