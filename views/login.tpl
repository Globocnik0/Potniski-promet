%rebase("base.tpl")

	<h1 class="text-center">For easier surfing and for further acces you may log in.</h1>
	<h3 class="text-center" style="color:rgb(255, 38, 0);">{{!alert}}</h3>
	<center>
		<div class="back">
			<div class="div-center">
				<div class="content">
					<form action="/login/" method="post">

						<div class="form-group">
							<label for="email">Email :</label> <input class="form-control-lg" id="email" name="email" placeholder="Vpiši elektronski naslov" type="email">
						</div>
						<br>
						
						<div class="form-group">
							<label for="password">Password :</label> <input class="form-control-lg" id="password" name="password" placeholder="Enter Password" required="" type="password">
						</div>
						
						<br>
						<div class="align-center">
							<button class="btn btn-success" type="submit">Log in</button>
						</div>
					</form>
				</div>
			</div>
		</div>
	</center>
