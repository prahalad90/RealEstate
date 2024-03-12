window.addEventListener('scroll', event => {
    let nav1 = document.querySelector('nav');
    if (window.scrollY > 50 & window.innerWidth>820) {
        document.getElementsByTagName('header')[0].classList.add('head');
        document.getElementById('logo').style.transform = "scale(0.8)";
        document.getElementById('logo').style.transition = "all 0.5s";
        nav1.classList.add('nav')
       
    }
    else {
        document.getElementsByTagName('header')[0].classList.remove('head');
        document.getElementById('logo').style.transform = "scale(1)"
        document.getElementById('logo').style.transition = "all 0.2s"
        nav1.classList.remove('nav')
    }
})

let a = 2
function toggle() {
    const aa = document.getElementById('menu');
    const ab = document.getElementById('close');
    for(i=1;i<a;i++){
        if (a%2==0){         
            document.getElementsByClassName('menus')[0].style.left = '0';
            document.getElementById('close').style.display = 'block'
            document.getElementById('menu').style.display = 'none'
            a++
        }
        else{        
            document.getElementsByClassName('menus')[0].style.left = '-100%';
            document.getElementById('close').style.display = 'none'
            document.getElementById('menu').style.display = 'block'
                a++
            }
            break;
    }
}


const x = document.getElementById('buy')
const y = document.getElementById('sell')
const z = document.getElementById('rent')
function buyForm(){
    document.querySelector('.form').setAttribute('style','background-color: rgba(0, 45, 75, 0.75);');
    x.setAttribute('style','transform:translateX(0px);transition:0.8s');
    y.setAttribute('style','transform:translate(-120%, 100%);transition:0.8s');
    z.setAttribute('style','transform:translate(-120%, 100%);transition:0.8s');    
}

function sellForm(){
    document.querySelector('.form').setAttribute('style','background-color: rgba(200, 45, 75, 0.75);');
    x.setAttribute('style','transform:translate(-120%, 100%);transition:0.8s');
    y.setAttribute('style','transform:translateY(-100% );transition:0.8s');
    z.setAttribute('style','transform:translate(-120%, 100% );transition:0.8s');

}
function rentForm(){
    document.querySelector('.form').setAttribute('style','background-color: rgba(0, 150, 45, 0.75);');
    x.setAttribute('style','transform:translate(-120%, 100%);transition:0.8s');
    y.setAttribute('style','transform:translate(-120%, 100%);transition:0.8s');
    z.setAttribute('style','transform:translateY(-200% );transition:0.8s');
}
