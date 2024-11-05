<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Equilibrium</title>
    <style>
        body {
            display: flex;
            font-family: Arial, sans-serif;
            justify-content: center;
            align-items: flex-start;
            height: 100vh;
            margin: 0;
            background-color: #e0e0e0;
        }
        #gameCanvas {
            border: 1px solid black;
            background-color: #f0f0f0;
        }
        #controlPanel {
            margin-left: 20px;
        }
        .control {
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <div>
        <h1 style="text-align: center;">Equilibrium</h1>
        <canvas id="gameCanvas" width="600" height="400"></canvas>
        <div id="controlPanel">
            <h3>Control Panel</h3>
            <div class="control">
                <label for="weight">Weight:</label>
                <input type="number" id="weight" value="10">
            </div>
            <div class="control">
                <label for="distance">Distance from Pivot:</label>
                <input type="number" id="distance" value="50">
            </div>
            <button id="addWeight">Add Weight</button>
            <button id="reset">Reset</button>
        </div>
    </div>
    <script src="script.js"></script>
</body>
</html>
