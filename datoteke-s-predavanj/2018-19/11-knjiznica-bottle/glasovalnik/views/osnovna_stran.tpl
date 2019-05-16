To je stran za glasovanje:

<h3>{{ vprasanje.besedilo }}</h3>

<form action="/glasuj/" method="POST">
    <ul>
    % for i, odgovor in enumerate(vprasanje.odgovori):
        <li><input type="radio" name="glas" value="{{ i }}">{{ odgovor.besedilo }}</li>
    % end
    </ul>
    <input type="submit" value="Glasuj">
</form>