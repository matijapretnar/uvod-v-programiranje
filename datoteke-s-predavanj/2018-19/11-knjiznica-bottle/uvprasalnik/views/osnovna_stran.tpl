<html>
  <head>
    <title>UVPrašalnik</title>
  </head>
  <body>
    % if vprasanje is None:
      <h3>Trenutno ni odprtega vprašanja</h3>
    % else:
      <h3>{{ vprasanje.besedilo }}</h3>
      <ul>
      % for indeks_odgovora, odgovor in enumerate(vprasanje.odgovori):
      <li>
        {{ odgovor.besedilo }}
        <small>
          ({{ odgovor.stevilo_glasov() }} glasov)
          <form action="/glasuj/" method="POST">
            <input type="hidden" value="{{ indeks_odgovora }}" name="indeks_odgovora">
            <input type="submit" value="glasuj">
          </form>
        </small>
      </li>
      % end
    % end
  </body>
</html>
