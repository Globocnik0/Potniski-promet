%rebase("base.tpl")

        <h1 style="color:rgb(59, 182, 110);">
            Here you can see your new as well as old purchases.
        </h1>

        <table>
            % for i, ticket in enumerate(tickets):
                % if ticket[5] == 1:
                % validity = 'checked'
                % else:
                % validity = 'unchecked'
                % end
            <tr> 
                <td>{{ticket[0]}} </td> <td>Purchase time: {{ticket[1]}}</td> <td>Valid until: {{ticket[2]}}</td> <td>Start: {{ticket[3]}} </td> <td>Stop: {{ticket[4]}} </td> <td><input type="checkbox" {{validity}} disabled></td>
                
            </tr>
            % end
        </table>



