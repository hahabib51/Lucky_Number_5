/** processForm: get data from form and make AJAX call to our API. */

async function processForm(evt) {
    evt.preventDefault();

    const name = $('#name').val();
    const year = $('#year').val();
    const email = $('#email').val();
    const color = $('#color').val();

    const json = JSON.stringify({ "name": name, "year": year, "email": email, "color": color });

    const res = await axios.post('http://127.0.0.1:5000/api/get-lucky-num', json, {
        headers: {
            'Content-Type': 'application/json'
        }
    });

    console.log(res.data)
    handleResponse(res);

}

/** handleResponse: deal with response from our lucky-num API. */

function handleResponse(res) {

    // Error handling and displaying the error messages
    if (res.data.errors) {
        if (res.data.errors.name) {
            error = res.data.errors.name[0];
            $('#name-err').text(error);
        }
        if (res.data.errors.year) {
            error = res.data.errors.year[0];
            $('#year-err').text(error);
        }
        if (res.data.errors.email) {
            error = res.data.errors.email[0];
            $('#email-err').text(error);
        }
        if (res.data.errors.color) {
            error = res.data.errors.color[0];
            $('#color-err').text(error);
        }
    } else {
        // Declaring variables for the data
        const num = res.data.num.num;
        const numFact = res.data.num.fact;
        const year = res.data.year.year;
        const yearFact = res.data.year.fact;

        const result = `Your lucky number is ${num}. ${numFact}
        Your birth year ${year} fact is ${yearFact}.`;

        $('#lucky-results').text(result);
    }
}


$("#lucky-form").on("submit", processForm);
