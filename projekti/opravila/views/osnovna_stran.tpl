<html>

<body>
    <h1>Opravila</h1>
    <h2>Najboljši projekt na svetu!</h2>

    % if neopravljena > 0:
    <h3>Zamuja ti že {{neopravljena}} opravil!</h3>
    % else:
    <h3>Vse si opravil!</h3>
    % end

    <h3>Aktualna opravila</h3>
    <ul>
        % for indeks, opravilo in enumerate(opravila):
        % if opravilo.opravljeno:
        <li><del>{{ opravilo.ime }}</del></li>
        % else:
        <li>
            {{ opravilo.ime }}
            <form method="POST" action="/opravi/">
                <input type="hidden" name="indeks" value="{{indeks}}">
                <input type="submit" value="opravi!">
            </form>
        </li>
        % end
        % end
    </ul>

    <form method="POST" action="/dodaj/">
        ime: <input type="text" name="ime">
        opis: <input type="text" name="opis">
        <input type="submit" value="dodaj!">
    </form>
</body>

</html>