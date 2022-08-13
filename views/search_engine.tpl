%rebase("base.tpl")

        <h1 style="color:rgb(59, 182, 110);">
            % if user:
            Greetings {{user}}! Choose a destination of your next travel.
            % end
        </h1>

        <center>
            <div class="back">
                <div class="div-center">
                    <div class="content">
                        <form action="/search/" method="post">
                            <div class="form-group">
                                <label for="station_1">Station 1 :</label> <input class="form-control-lg" id="station_1" name="station_1" placeholder="Enter station_1" required="" type="text">
                            </div>
                            <div class="form-group">
                                <label for="station_2">Station 2 :</label> <input class="form-control-lg" id="station_2" name="station_2" placeholder="Enter station_2" required="" type="text">
                            </div>
                            
                            <div class="align-center">
                                <button class="btn btn-success" type="submit">Search</button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </center>
