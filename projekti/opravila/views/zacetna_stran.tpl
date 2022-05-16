% rebase('osnova.tpl')
<!-- Main container -->
<nav class="level">
    <div class="level-left">
        <div class="buttons has-addons field is-horizontal">
            % for id_kategorije, kategorija in enumerate(kategorije):
            <a href="/kategorija/{{id_kategorije}}/" class="button" name="id_kategorije" value="{{id_kategorije}}">
                {{kategorija.ime}}
                <span class="tag is-rounded">{{kategorija.stevilo_neopravljenih()}}</span>
            </a>
            % end
        </div>

    </div>

    <div class="level-right">
            <div class="level-item">
                <a class="button is-info" href="/dodaj-kategorijo/">dodaj kategorijo</a>
            </div>
        </form>
    </div>
</nav>
