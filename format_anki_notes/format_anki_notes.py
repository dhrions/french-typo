# format_anki_notes/format_anki_notes.py
from aqt import mw, gui_hooks
from aqt.utils import showInfo
from aqt.qt import QAction, QMessageBox
from aqt.editor import Editor
from .main import format_text
from .logger import get_logger

def format_current_note(editor: Editor) -> None:
    """Formate la note actuelle avec les règles typographiques françaises."""
    try:
        note = editor.note
        modified = False
        for field_name in note.keys():
            if field_name in note:
                original_text = note[field_name]
                formatted_text = format_text(original_text)
                if not isinstance(formatted_text, str):
                    formatted_text = original_text
                if formatted_text != original_text:
                    note[field_name] = formatted_text
                    modified = True
        if modified:
            mw.col.update_note(note)
            editor.loadNote()
            showInfo("Note formatée avec succès !")
            if hasattr(mw, 'format_anki_notes_logger'):
                get_logger.info(f"Note {note.id} formatée avec succès.")
        else:
            showInfo("Aucune modification nécessaire.")
            if hasattr(mw, 'format_anki_notes_logger'):
                get_logger.debug("Aucune modification nécessaire pour cette note.")
    except Exception as e:
        showInfo(f"Erreur lors du formatage : {str(e)}")
        if hasattr(mw, 'format_anki_notes_logger'):
            get_logger.error(f"Erreur détaillée : {str(e)}", exc_info=True)
        else:
            print(f"[FormatAnkiNotes] Erreur détaillée : {str(e)}")

def add_format_button_to_editor(editor: Editor) -> None:
    """Ajoute un bouton 'Formater' à l'éditeur de notes, sans doublons."""
    for link in getattr(editor, '_links', []):
        if isinstance(link, dict) and link.get('cmd') == "format_note":
            if hasattr(mw, 'format_anki_notes_logger'):
                get_logger.debug("Bouton 'Formater' déjà présent dans l'éditeur.")
            return

    editor.addButton(
        icon=None,
        cmd="format_note",
        func=lambda e=editor: format_current_note(e),
        tip="Formater la note selon les règles typographiques françaises (n°, espaces insécables, etc.)",
        label="Formater",
        keys="Ctrl+Shift+F",
    )
    if hasattr(mw, 'format_anki_notes_logger'):
        get_logger.info("Bouton 'Formater' ajouté à l'éditeur.")

def format_selected_notes_in_browser(browser):
    logger = get_logger()
    logger.info("format_selected_notes_in_browser appelé !")

    try:
        if not hasattr(browser, 'selectedNotes'):
            logger.warning("browser.selectedNotes non disponible.")
            showInfo("Veuillez sélectionner des notes dans le navigateur.")
            return

        selected_notes = browser.selectedNotes()
        logger.info(f"Notes sélectionnées : {selected_notes}")

        if not selected_notes:
            showInfo("Aucune note sélectionnée.")
            return

        confirm = QMessageBox.question(
            browser,
            "Formater les notes",
            f"Voulez-vous vraiment formater {len(selected_notes)} notes ?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if confirm != QMessageBox.StandardButton.Yes:
            logger.info("Formatage annulé par l'utilisateur.")
            return

        count = 0
        for note_id in selected_notes:
            try:
                note = mw.col.get_note(note_id)
                logger.info(f"Traitement de la note {note_id} (champs : {note.keys()})")
                modified = False
                for field_name in note.keys():
                    original_html = note[field_name]
                    formatted_html = format_text(original_html)
                    if formatted_html != original_html:
                        note[field_name] = formatted_html
                        modified = True
                        logger.info(f"Champ '{field_name}' modifié.")
                if modified:
                    mw.col.update_note(note)
                    count += 1
                    logger.info(f"Note {note_id} formatée.")
            except Exception as e:
                logger.error(f"Erreur pour la note {note_id} : {e}", exc_info=True)

        showInfo(f"{count} notes formatées avec succès !")
        logger.info(f"{count} notes formatées avec succès.")

    except Exception as e:
        logger.error(f"Erreur inattendue : {e}", exc_info=True)
        showInfo(f"Erreur inattendue : {e}")




def add_format_menu_to_browser(browser):
    logger = get_logger()
    logger.info("Hook browser_will_show déclenché !")

    try:
        menu_notes = None
        for action in browser.menuBar().actions():
            if action.text() == "&Notes":
                menu_notes = action.menu()
                logger.info("Menu 'Notes' trouvé.")
                break

        if not menu_notes:
            logger.error("Menu 'Notes' introuvable dans le navigateur.")
            return

        # Vérifie si l'action existe déjà
        for existing_action in menu_notes.actions():
            if existing_action.text() == "Formater les notes sélectionnées":
                logger.info("L'action 'Formater les notes sélectionnées' existe déjà.")
                return

        # Fonction intermédiaire pour capturer le browser
        def on_format_selected_notes():
            logger.info("Callback 'on_format_selected_notes' appelé !")
            try:
                format_selected_notes_in_browser(browser)
            except Exception as e:
                logger.error(f"Erreur dans le callback : {e}", exc_info=True)
                showInfo(f"Erreur : {e}")

        # Crée l'action
        new_action = QAction("Formater les notes sélectionnées", mw)
        new_action.triggered.connect(on_format_selected_notes)
        menu_notes.addAction(new_action)
        logger.info("Action 'Formater les notes sélectionnées' ajoutée avec succès.")

    except Exception as e:
        logger.error(f"Erreur dans add_format_menu_to_browser : {e}", exc_info=True)



def initialize_addon():
    logger = get_logger()
    logger.info("Initialisation de l'add-on...")

    gui_hooks.editor_did_init.append(add_format_button_to_editor)
    gui_hooks.browser_will_show.append(add_format_menu_to_browser)
    logger.info("Hooks enregistrés.")


