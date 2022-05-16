% rebase('osnova.tpl')
<!-- Main container -->
<nav class="level">
    <div class="level-left">
        <div class="buttons has-addons field is-horizontal">
            % for id_kategorije, kategorija in enumerate(kategorije):
            % if kategorija == aktualna_kategorija:
            <a class="button is-primary is-selected" name="id_kategorije" value="{{id_kategorije}}">
                {{kategorija.ime}}
                <span class="tag is-rounded">{{kategorija.stevilo_neopravljenih()}}</span>
            </a>
            % else:
            <a href="/kategorija/{{id_kategorije}}/" class="button" name="id_kategorije" value="{{id_kategorije}}">
                {{kategorija.ime}}
                <span class="tag is-rounded">{{kategorija.stevilo_neopravljenih()}}</span>
            </a>
            % end
            % end
        </div>

    </div>

    <div class="level-right">
        <!-- <div class="level-item">
            <p class="subtitle is-5">
                <strong>123</strong> posts
            </p>
        </div> -->
            <div class="level-item">
                <a class="button is-info" href="/dodaj-kategorijo/">dodaj kategorijo</a>
            </div>
        </form>
    </div>
</nav>

% if aktualna_kategorija:

<table class="table is-hoverable is-fullwidth">
    <thead>
        <tr>
            <form method="POST" action="/dodaj-opravilo/{{id_aktualne_kategorije}}/">
                <td></td>
                <td>
                    <div class="control has-icons-left">
                        <input class="input is-small" type="text" name="opis" placeholder="opis">
                        <span class="icon is-small is-left">
                            <i class="far fa-clipboard-check"></i>
                        </span>
                    </div>
                </td>
                <td>
                    <div class="control has-icons-left">
                        <input class="input is-small" type="text" name="rok" placeholder="rok">
                        <span class="icon is-small is-left">
                            <i class="far fa-calendar-alt"></i>
                        </span>
                    </div>
                </td>
                <td>
                    <div class="control">
                        <button class="button is-info is-small">dodaj</button>
                    </div>
                </td>
            </form>
        </tr>
    </thead>
    <tbody>
        % for id_opravila, opravilo in enumerate(aktualna_kategorija.opravila):
        <tr>
            <td>
                <form method="POST" action="/opravi/{{id_aktualne_kategorije}}/{{id_opravila}}/">
                    <button class="button is-white">
                        <span class="icon is-small">
                            % if opravilo.opravljeno:
                            <i class="far fa-check-square"></i>
                            % else:
                            <i class="far fa-square"></i>
                            % end
                        </span>
                    </button>
                </form>
            </td>
            <td>{{ opravilo.opis }}</td>
            <td>{{ opravilo.rok }}</td>
            <td></td>
        </tr>
        % end
    </tbody>
</table>

% else:

<p>Nimate še nobenega spiska. <a href="/dodaj-kategorija/">Dodajte ga!</a></p>