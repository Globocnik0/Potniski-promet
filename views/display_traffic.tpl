%rebase("base.tpl")

        <h1 style="color:rgb(59, 182, 110);">
            Congratulations, you can now check out the traffic for your selected destination.
        </h1>

        <table>
            % for (ime, cas) in traffic_data:
            <tr> 
                <td>Vstopna postaja: {{ime}} Cas: {{cas}}</td>
            </tr>
            % end
        </table>