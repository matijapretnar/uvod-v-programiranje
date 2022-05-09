% rebase("osnova.tpl")

<h1>Dobrodošel v seznamu opravil</h1>

Tu je tvoj seznam kategorij:
<ul>
% for id_kategorije, kategorija in enumerate(kategorije):
    <li>
        <a href="/kategorija/{{ id_kategorije }}/">{{ kategorija.ime }}</a>
        % if kategorija.stevilo_zamujenih():
        <strong>zamujenih opravil: {{ kategorija.stevilo_zamujenih() }}</strong>
        % end
    </li>
% end
</ul>
