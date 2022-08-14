%rebase("base.tpl")

        <h1 style="color:rgb(59, 182, 110);">
            % if username:
            Greetings {{username}}! Choose a destination of your next travel.
            % else:
            Greetings fellow passenger! Choose a destination of your next travel.
            % end
        </h1>

        <center>
            <div class="back">
                <div class="div-center">
                    <div class="content">
                        <form action="/search/" method="post">
                            <!-- <div class="form-group">
                                <label for="station_1">Station 1 :</label> <input class="form-control-lg" id="station_1" name="station_1" placeholder="Enter station_1" required="" type="text">
                            </div> -->
                              
                            <label for="station_1">Starting station:</label>
                                <select name="station_1" id="station_1">
                                    <option value="Ljubljana">Ljubljana</option>
                                    <option value="Celje">Celje</option>
                                    <option value="Kranj">Kranj</option>                  
                                    <option value="Koper">Koper</option>
                                    <option value="Velenje">Velenje</option>
                                    <option value="Novo_mesto">Novo Mesto</option>
                                    <option value="Ptuj">Ptuj</option>
                                    <option value="Trbovlje">Trbovlje</option>
                                    <option value="Kamnik">Kamnik</option>
                                    <option value="Nova_Gorica">Nova Gorica</option>
                                    <option value="Domžale">Domžale</option>
                                    <option value="Jesenice">Jesenice</option>
                                    <option value="Škofja_Loka">Škofja Loka</option>
                                    <option value="Murska_Sobota">Murska Sobota</option>
                                    <option value="Izola">Izola</option>
                                    <option value="Postojna">Postojna</option>
                                    <option value="Logatec">Logatec</option>
                                    <option value="Vrhnika">Vrhnika</option>
                                    <option value="Kočevje">Kočevje</option>
                              </select>

                            <label for="station_2">Ending station:</label>
                              <select name="station_2" id="station_2">
                                  <option value="Ljubljana">Ljubljana</option>
                                  <option value="Celje">Celje</option>
                                  <option value="Kranj">Kranj</option>                  
                                  <option value="Koper">Koper</option>
                                  <option value="Velenje">Velenje</option>
                                  <option value="Novo_mesto">Novo Mesto</option>
                                  <option value="Ptuj">Ptuj</option>
                                  <option value="Trbovlje">Trbovlje</option>
                                  <option value="Kamnik">Kamnik</option>
                                  <option value="Nova_Gorica">Nova Gorica</option>
                                  <option value="Domžale">Domžale</option>
                                  <option value="Jesenice">Jesenice</option>
                                  <option value="Škofja_Loka">Škofja Loka</option>
                                  <option value="Murska_Sobota">Murska Sobota</option>
                                  <option value="Izola">Izola</option>
                                  <option value="Postojna">Postojna</option>
                                  <option value="Logatec">Logatec</option>
                                  <option value="Vrhnika">Vrhnika</option>
                                  <option value="Kočevje">Kočevje</option>
                            </select>
                            

                            <!-- <div class="form-group">
                                <label for="station_2">Station 2 :</label> <input class="form-control-lg" id="station_2" name="station_2" placeholder="Enter station_2" required="" type="text">
                            </div> -->
                            
                            <div class="align-center">
                                <button class="btn btn-success" type="submit">Search</button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </center>
