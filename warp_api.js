async function set_window_name(name) {
    await window.pywebview.api.set_window_name(name);
}

async function set_size(w, h) {
    await window.pywebview.api.set_size(w, h);
}

async function create_stray_menu(name_item) {
    await window.pywebview.api.create_stray_menu(name_item);
}

async function create_stray_icon(name, des, icon_path) {
    await window.pywebview.api.create_stray_icon(name, des, icon_path);
}

async function developer_mode() {
    await window.pywebview.api.developer_mode();
}
