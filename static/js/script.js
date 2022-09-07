var cta = document.querySelector(".cta");
var check = 0;

cta.addEventListener('click', function(e){
    var text = e.target.nextElementSibling;
    var loginText = e.target.parentElement;
    text.classList.toggle('show-hide');
    loginText.classList.toggle('expand');
    if(check == 0)
    {
        cta.innerHTML = "<i class=\"fas fa-chevron-up\"></i>";
        check++;
    }
    else
    {
        cta.innerHTML = "<i class=\"fas fa-chevron-down\"></i>";
        check = 0;
    }

})

const gsBtn = document.querySelector('.GS-btn')
const login = document.querySelector('.login-text')
const textContent = document.querySelector('.text')

gsBtn.addEventListener('click', () => {
    login.classList.toggle('expand');
    textContent.classList.add('show-hide');
})

let link = document.querySelector('.login-link');
let loginPanel = document.querySelector('.login-panel');
let link2 = document.querySelector('.login-link2')

link.addEventListener('click', () => {
    loginPanel.classList.add('show-login');
    login.classList.add('show-hide');
})

link2.addEventListener('click', () => {
    loginPanel.classList.remove('show-login');
})