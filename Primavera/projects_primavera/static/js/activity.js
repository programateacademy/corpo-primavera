function completed(obj) {
    elem=obj.parentNode.parentNode.parentNode;
    elem.style.background=obj.checked ? '#279704' : '';
  }

  function pending(obj) {
    elem=obj.parentNode.parentNode.parentNode;
    elem.style.background=obj.checked ? '#F5A601' : '';
  }

  