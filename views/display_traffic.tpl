%rebase("base.tpl")

        <h1 style="color:rgb(59, 182, 110);">
            Congratulations, you can now check out the traffic for your selected destination.
        </h1>

        <table>
            % for i, (ime, cas) in enumerate(traffic_data):
            <tr> 
                % if i%2 == 0:
                <td>Vstopna postaja: {{ime}} </td> <td>Cas: {{cas}}</td> <td rowspan="2">Buy ticket</td>
                % else:
                <td>Iztopna postaja: {{ime}} </td> <td>Cas: {{cas}}</td>
                
                % end
            </tr>
            % end
        </table>