$(document).ready(function() {
    let x = 1; // Initialize the counter for dynamic IDs

    // Add a new row to the table
    $('#add_button').click(function() {
        let newRow = `
        <tr>
            <td style="padding: 0; margin: 0;">
               <input type="text" 
                    name="account_code${x}" 
                    id="account_code${x}"
                    class="account_code"
                    step="0.01"
                     />
            </td>

            <td style="padding: 0; margin: 0;">
                    <input
                        type="text"
                        name="accountTitle${x}"
                        id="accountTitle${x}"
                        onchange="myFunction2()"
                    />
                </td>
                <td style="padding: 0; margin: 0;">
                    <input
                        type="text"
                        name="amount${x}"
                        id="amount${x}"
                        class="amount"
                        onchange="myFunction2()"
                        step="any"
                    />
                </td>
                <td style="padding: 0; margin: 0;">
                    <input
                        type="text"
                        name="credit_amount${x}"
                        id="credit_amount${x}"
                        class="credit_amount"
                        onchange="myFunction2()"
                        step="any"
                    />
                </td>

                 <td style="padding: 0; margin: 0;">
                    <input
                        type="text"
                        name="chart_of_account_id${x}"
                        id="chart_of_account_id${x}"
                        class="chart_of_account_id"
                        
                        hidden
                    />
                </td>
                
            <td><button type="button" class="btn btn-danger remove-row">Remove</button></td>
        </tr>`;
        
        $('#addrow').append(newRow);
        x++; // Increment the counter for the next row
        logAllAccountTitles();
       
    });

    // Remove a row from the table (applies to both existing and dynamically added rows)
    $(document).on('click', '.remove-row', function() {
        $(this).closest('tr').remove();
        logAllAccountTitles();
    });

     // Bind myFunction2 to change events of .amount and .credit_amount fields
    $(document).on('change', '.amount, .credit_amount', myFunction2);

     // Log accountTitle values on page load
     logAllAccountTitles();
});

// Function to log all accountTitle values
function logAllAccountTitles() {
    // Get all elements with names starting with 'accountTitle'
    let accountTitleList = document.querySelectorAll('[id^="accountTitle"]');

    // Iterate through each element and log its ID and value
    accountTitleList.forEach(function(input) {
        console.log(`ID: ${input.id}, Value: ${input.value}`); // Log each ID and value
    });
}


// this function is for autocomplete row
jQuery.noConflict();
jQuery(document).ready(function($) {
    $(document).on('focus', '[id^="accountTitle"]', function() {
        $(this).autocomplete({
            source: function(request, response) {
                $.ajax({
                    url: "/api-autocomplete-chart-of-account/", // Replace with your actual endpoint
                    data: { term: request.term },
                    dataType: "json",
                    success: function(data) {
                        response(data);
                    },
                    error: function(err) {
                        console.error("Error fetching autocomplete data:", err);
                    }
                });
            },
            minLength: 0,
            select: function(event, ui) {
                $(this).val(ui.item.value);
                // Ensure you set the correct account_no field related to the focused accountTitle
                $(this).closest('tr').find('[id^="account_code"]').val(ui.item.chart_of_account_code);
                $(this).closest('tr').find('[id^="chart_of_account_id"]').val(ui.item.id);
                return false;
            }
        });
    });
});


// this function is to check that debit and credit balance balance is equal 

function myFunction2() {
    document.querySelector("#submiBTN").disabled = true;
    
    var total = 0.0;
    let debitsum = 0;
    let creditsum = 0;

    // Process amount fields
    let debitList = document.getElementsByClassName('amount');
    for (let i of debitList) {
        let debitValue = parseFloat(parseFormattedNumber(i.value));
        if (!isNaN(debitValue)) {
            debitsum += debitValue;
        }
    }
    let debitsum2 = parseFloat(debitsum).toFixed(2);
    
    // Process credit_amount fields
    let creditList = document.getElementsByClassName('credit_amount');
    for (let i of creditList) {
        let creditValue = parseFloat(parseFormattedNumber(i.value));
        if (!isNaN(creditValue)) {
            creditsum += creditValue;
        }
    }
    let creditsum2 = parseFloat(creditsum).toFixed(2);

    // Calculate total
    total = parseFloat(debitsum2) - parseFloat(creditsum2);

    // Enable or disable the submit button based on the total
    if (total === 0) {
        document.getElementById("submiBTN").disabled = false;
    } else {
        document.getElementById("submiBTN").disabled = true;
    }
}


// Function to format number with thousand separator
function formatNumberWithSeparator(value) {
    return parseFloat(value).toLocaleString('en-US', {
        minimumFractionDigits: 2,
        maximumFractionDigits: 2
    });
}

// Function to remove thousand separators and convert back to a number
function parseFormattedNumber(value) {
    return value.replace(/,/g, '');
}

myFunction2()


