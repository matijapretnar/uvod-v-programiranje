% rebase('bootstrap.tpl')
% if vprasanje is None:
  <h3>Trenutno ni odprtega vprašanja</h3>
% else:
  <h3 class="poudari">{{ vprasanje.besedilo }}</h3>
  <ul class="list-group">
  % for indeks_odgovora, odgovor in enumerate(vprasanje.odgovori):
  <li class="list-group-item">
    {{ odgovor.besedilo }}
    <span class="badge badge-light">
      {{ odgovor.stevilo_glasov() }} glasov
    </span>
      <form action="/glasuj/" method="POST">
        <input type="hidden" value="{{ indeks_odgovora }}" name="indeks_odgovora">
        <input class="btn btn-light" type="submit" value="glasuj">
      </form>
  </li>
  % end
% end
