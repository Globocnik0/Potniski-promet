%rebase("base.tpl")

        <h1 style="color:rgb(59, 182, 110);">
            Are you sure you want to buy this ticket?
        </h1>

        <h3 style="color:rgb(59, 182, 110);">
            If you miss your termine you can use the card at other times too!
        </h3>
    
        <table>
            <tr> 
                <td>Starting location: {{station_1}} </td> <td>Ending station: {{station_2}}</td> <td>Ticket type: {{ticket_type}}</td> <td>Price: {{price}} € </td> <td><a href='/buy_ticket/{{station_1}}/{{station_2}}/{{type}}/' >Buy Ticket</a></td>
            </tr>
        </table>



