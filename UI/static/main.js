var login = document.getElementById('login');
var wrongUsername = document.getElementById('wrong-name');
var wrongPassword = document.getElementById('wrong-password');


login.addEventListener('submit', function(e){
    e.preventDefault();

    if (e.target.name.value == 'admin' && e.target.password.value == 'admin'){
        e.target.name.value = '';
        e.target.name.value = '';
        window.location.href = '../SENDIT/UI/templates/admin.html'
    } else if (e.target.name.value == 'client' && e.target.password.value == 'client'){
        e.target.name.value = '';
        e.target.name.value = '';
        window.location.href = '../SENDIT/UI/templates/user.html';
    }

    if (e.target.name.value == '' || e.target.password.value == ''){
        wrongUsername.style.display = 'block';
        wrongUsername.innerText = 'Provide Username and Password';
    } else if (e.target.name.value != 'admin' || e.target.password.value != 'admin'){
        wrongUsername.style.display = 'block';
        wrongUsername.innerText = 'wrong username or password';
    }

    if (e.target.name.value == '' || e.target.password.value == ''){
        wrongPassword.style.display = 'block';
        wrongPassword.innerText = 'Provide Username and Password';
    } else if (e.target.name.value != 'client' || e.target.password.value != 'client'){
        wrongPassword.style.display = 'block';
        wrongPassword.innerText = 'wrong username or password';
    }

   
});