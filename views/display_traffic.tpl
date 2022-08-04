%rebase("base.tpl")

        <h1 style="color:rgb(59, 182, 110);">
            Congratulations, you can now check out the traffic for your selected destination.
        </h1>

        <table>
            % for row in traffic_data:
            <tr> 
                <td>{{row}}</td>
            </tr>
            % end
        </table>