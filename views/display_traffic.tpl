%rebase("base.tpl")

        <h1 style="color:rgb(59, 182, 110);">
            Congratulations, you can now check out the traffic for your selected destination.
        </h1>

        <table>
            % for i, (ime, cas, razdalja) in enumerate(traffic_data):
            <tr> 
                % if i%2 == 0:
                <td>Vstopna postaja: {{ime}} </td> <td>Cas: {{cas}}</td>  <td rowspan="2"> <a href='' >Buy ticket</a> </td>
                <td>Razdalja: {{razdalja}} km </td>
                % else:
                <td>Iztopna postaja: {{ime}} </td> <td>Cas: {{cas}}</td>
                
                % end
            </tr>
            % end
        </table>

        <a href='' >Buy mothly ticket for this relation</a>
        <a href='' >Buy student mothly ticket for this relation</a>
        <a href='' >Buy pensioner monthly ticket for this relation</a>