
const dis = document.querySelector('div')
let lood = async ()=>{
    let iem = await fetch('http://127.0.0.1:800/api/art/',{
        'method':'GET',
        headers :{
            'Content-type':'application/json',
            'Authorization':'Token cf2bc8295475bf19b9cbb210a3299d120b318518'

        }
    })
    let jesd = await iem.json(
        // method:post
    )
    // console.log(iem);
    // console.log(jesd);
    for (let i = 0; jesd.length > i ; i++) {
        let room = jesd[i];
        let inns = `<small>
       <h1> ${room.name}</h1> 
        </small>
        `
        dis.innerHTML += inns
        
    }
}
lood()