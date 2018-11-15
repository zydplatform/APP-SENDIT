var signup = document.getElementById('signup');

signup.addEventListener('submit',function(p){
    p.preventDefault();
    if (p.target.name.value != '' && p.target.password.value != ''
        && p.target.email.value !=''&& p.target.phone.value !=''&& p.target.confirm.value !=''){
        p.target.name.value = '';
        p.target.email.value = '';
        p.target.phone.value = '';
        p.target.password.value = '';
        p.target.confirm.value = '';        
        window.location.href = '../../index.html';
}
});