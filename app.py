import streamlit as st
from deep_translator import GoogleTranslator
from deep_translator.exceptions import (
    ApiKeyException,
    AuthorizationException,
    InvalidSourceOrTargetLanguage,
    NotValidPayload,
    RequestError,
    TooManyRequests,
)

st.set_page_config(
    page_title="AI Language Translation Tool",
    page_icon="🌍",
    layout="centered",
)

st.title("🌍 AI Language Translation Tool")
st.write(
    "Translate text between supported languages using the Google Translate "
    "service through the `deep-translator` Python library."
)

st.info(
    "This project needs an internet connection. Translation is handled by an "
    "external service, so avoid entering passwords or other sensitive information."
)

@st.cache_data
def get_languages():
    """Return supported language names and their language codes."""
    return GoogleTranslator().get_supported_languages(as_dict=True)

try:
    languages = get_languages()
except Exception as exc:
    st.error(
        "The language list could not be loaded. Check your internet connection "
        "and try restarting the app."
    )
    st.caption(f"Technical details: {exc}")
    st.stop()

language_names = sorted(languages.keys())
language_names_with_auto = ["auto"] + language_names

# Keep selections in session state so the Swap button works across reruns.
if "source_language" not in st.session_state:
    st.session_state.source_language = "auto"
if "target_language" not in st.session_state:
    st.session_state.target_language = "english"
if "input_text" not in st.session_state:
    st.session_state.input_text = ""
if "translated_text" not in st.session_state:
    st.session_state.translated_text = ""

st.subheader("Translation settings")
col1, col2 = st.columns(2)

with col1:
    source_options = language_names_with_auto
    source_default = (
        st.session_state.source_language
        if st.session_state.source_language in source_options
        else "auto"
    )
    source_language = st.selectbox(
        "Translate from",
        options=source_options,
        index=source_options.index(source_default),
        format_func=lambda value: "Auto-detect" if value == "auto" else value.title(),
        key="source_language_select",
    )

with col2:
    target_default = (
        st.session_state.target_language
        if st.session_state.target_language in language_names
        else ("english" if "english" in language_names else language_names[0])
    )
    target_language = st.selectbox(
        "Translate to",
        options=language_names,
        index=language_names.index(target_default),
        format_func=lambda value: value.title(),
        key="target_language_select",
    )

st.session_state.source_language = source_language
st.session_state.target_language = target_language

st.subheader("Enter your text")
input_text = st.text_area(
    "Text to translate",
    key="input_text",
    height=180,
    max_chars=5000,
    placeholder="Example: Namaste! Aap kaise hain?",
    help="For this beginner project, input is limited to 5,000 characters.",
)
st.caption(f"{len(input_text)} / 5,000 characters")

def clear_fields():
    """Clear input and output before Streamlit reruns the page."""
    st.session_state.input_text = ""
    st.session_state.translated_text = ""

button_col1, button_col2 = st.columns(2)
with button_col1:
    translate_clicked = st.button(
        "🌐 Translate",
        type="primary",
        use_container_width=True,
    )
with button_col2:
    st.button("🧹 Clear", use_container_width=True, on_click=clear_fields)

if translate_clicked:
    if not input_text.strip():
        st.warning("Please enter some text before translating.")
        st.session_state.translated_text = ""
    elif source_language != "auto" and source_language == target_language:
        st.warning("Choose two different languages, or use Auto-detect as the source.")
        st.session_state.translated_text = ""
    else:
        try:
            translator = GoogleTranslator(
                source=source_language,
                target=target_language,
            )
            with st.spinner("Translating your text..."):
                result = translator.translate(input_text.strip())
            if not result:
                st.warning("The translation service returned an empty result.")
                st.session_state.translated_text = ""
            else:
                st.session_state.translated_text = result
                st.success("Translation completed!")
        except TooManyRequests:
            st.error("Too many requests were sent. Wait a little and try again.")
        except InvalidSourceOrTargetLanguage:
            st.error("One of the selected languages is not supported.")
        except (RequestError, ApiKeyException, AuthorizationException, NotValidPayload) as exc:
            st.error("The translation service could not process the request.")
            st.caption(f"Technical details: {exc}")
        except Exception as exc:
            st.error(
                "Translation failed. Check your internet connection, try shorter "
                "text, or try again later."
            )
            st.caption(f"Technical details: {exc}")

if st.session_state.translated_text:
    st.divider()
    st.subheader("Translated text")
    st.text_area(
        "Result",
        value=st.session_state.translated_text,
        height=180,
        disabled=True,
    )
    st.download_button(
        "⬇️ Download translation (.txt)",
        data=st.session_state.translated_text,
        file_name="translation.txt",
        mime="text/plain",
        use_container_width=True,
    )

st.divider()
st.caption("Built with Python, Streamlit, and deep-translator | CodeAlpha AI Internship Task 1")
