% rebase("osnova.tpl")

<h1>{{ kategorija.ime }}</h1>

Tu je seznam opravil:
<ul>
    <li>
    <form method="POST" action="/dodaj/{{ id_kategorije }}/">
        <input name="opis_novega_opravila" placeholder="Opis opravila">
        <button>DODAJ</button>
    </form>
    </li>
    % for id_opravila, opravilo in enumerate(kategorija.opravila):
    <li>
        % if opravilo.opravljeno:
        <del>{{ opravilo.opis }}</del>
        % else:
        {{ opravilo.opis }}
        <form method="POST" action="/opravi/{{ id_kategorije }}/{{ id_opravila }}/">
            <button>OPRAVI</button>
        </form>
        % end
    % end
    </li>
</ul>
