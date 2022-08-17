%rebase("base.tpl")

        <h1 style="color:rgb(59, 182, 110);">
            Congratulations, you can now check out the traffic for your selected destination.
        </h1>

        <table>
            % station_1 = traffic_data[0][0]
            % station_2 = traffic_data[1][0]
            % for i, (ime, cas) in enumerate(traffic_data):
            <tr> 
                % if i%2 == 0:
                <td>Vstopna postaja: {{ime}} </td> <td>Cas: {{cas}}</td> <td rowspan="2"> <a href='/buy_ticket/{{station_1}}/{{station_2}}/5/' >Buy ticket</a> </td>
                % else:
                <td>Iztopna postaja: {{ime}} </td> <td>Cas: {{cas}}</td>
                
                % end
            </tr>
            % end
        </table>

        <a href='/buy_ticket/{{station_1}}/{{station_2}}/4/' >Buy student mothly ticket for this relation</a>
        <a href='/buy_ticket/{{station_1}}/{{station_2}}/3/' >Buy mothly ticket for this relation</a>
        <a href='/buy_ticket/{{station_1}}/{{station_2}}/2/' >Buy pensioner monthly ticket for this relation</a>
        <a href='/buy_ticket/{{station_1}}/{{station_2}}/1/' >Buy yearly ticket for this relation</a>