%rebase("base.tpl")

        <h1 style="color:rgb(59, 182, 110);">
            Congratulations, you can now check out the traffic for your selected destination.
        </h1>

        <table>
            % for i, (ime, cas) in enumerate(traffic_data):
            <tr> 
                <td>
                % if i%2 == 0:
                    Vstopna postaja: {{ime}} Cas: {{cas}}
                % else:
                    Iztopna postaja: {{ime}} Cas: {{cas}}
                
                % end
                
                </td>
                
            </tr>
            % end
        </table>