$("#show_password_button").click((event) => { 
    event.preventDefault()
    let password = $("#show_password_button").attr('data-password')
    let nama_webinar = $("#show_password_button").attr('data-nama-webinar')
    swal({
        title: `Password Room Webinar ${nama_webinar} :`,
        text: `${password}`
    })
})