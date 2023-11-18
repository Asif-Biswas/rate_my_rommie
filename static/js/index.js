const navbtn = document.getElementById('nav-btn');
const navinput = document.getElementById('nav-input');
const headtext = document.getElementById('head-text');
const headtext2 = document.getElementById('head-text2');
const headerinput = document.getElementById('header-input');
const search_form = document.getElementById('search-form');
const nav_search_form = document.querySelectorAll('.nav-search-form');

const cngNavElemets = (e) => {
    navbtn.innerText = e
    if (navbtn.innerText == 'Address') {
        nav_search_form.forEach((e) => {
            e.action = '/search-address'
        })
    } else {
        nav_search_form.forEach((e) => {
            e.action = '/search-roommate'
        })
    }
}
const cngHeadText = () => {
    if (headtext.innerText == 'Welcome to Roommate Finder') {
        headtext.innerText = 'Welcome to Address Finder'
        headtext2.innerText = 'Find your perfect Roommate today!'
        headerinput.placeholder = 'Enter address name'
        search_form.action = '/search-address'
    }
    else {
        headtext.innerText = 'Welcome to Roommate Finder'
        headtext2.innerText = 'Find your perfect Address today!'
        headerinput.placeholder = 'Enter Roommate name'
        search_form.action = '/search-roommate'
    }

}

// check if search-address in url
const url = window.location.href;
if (url.includes('search-address')) {
    cngNavElemets('Address')
}

const accordionSidebar = document.querySelector('#accordionSidebar');
if (window.innerWidth > 768) {
    accordionSidebar.classList.remove('toggled');
}

const select_style = document.querySelectorAll('.select-style');
select_style.forEach((e) => {
    e.addEventListener('change', () => {
        const value = e.value;
        if (value == 'Roommate') {
            cngNavElemets('Roommate')
        } else {
            cngNavElemets('Address')
        }
    })
})