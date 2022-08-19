%rebase("base.tpl")

    <h1 style="color:rgb(59, 182, 110);">
        Congratulations, you can now check out the traffic for your selected destination.
    </h1>
        % if not traffic_data == []:
    <table>
            % station_1 = traffic_data[0][0]
            % station_2 = traffic_data[1][0]
            % for i, (ime, cas, razdalja) in enumerate(traffic_data):
            <tr> 
                % if i%2 == 0:
                <td>Start: {{ime}} </td> <td>Time: {{cas}}</td> <td rowspan="2"> <a href='/ticket_preview/{{station_1}}/{{station_2}}/5/' >Preview Ticket</a> </td> <td rowspan="2">Distance: {{razdalja}} km </td>
                % else:
                <td>Stop: {{ime}} </td> <td>Time: {{cas}}</td>
                % end
            </tr>
            % end
    </table>

    <a href='/ticket_preview/{{station_1}}/{{station_2}}/4/' >Preview student mothly ticket for this relation</a>
    <a href='/ticket_preview/{{station_1}}/{{station_2}}/3/' >Preview mothly ticket for this relation</a>
    <a href='/ticket_preview/{{station_1}}/{{station_2}}/2/' >Preview pensioner monthly ticket for this relation</a>
    <a href='/ticket_preview/{{station_1}}/{{station_2}}/1/' >Preview yearly ticket for this relation</a>   
        % else:

    <h2 style="color:rgb(59, 182, 110);">
        There is no traffic between your selected destinations. Choose a different city.
    </h2>

        % end
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    