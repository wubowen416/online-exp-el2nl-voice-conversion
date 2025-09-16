import time

import numpy as np
import streamlit as st

# np.random.seed(1234)


def get_url(idx: str, name: str):
    url = f"https://wu-cloud-bucket.s3.ap-northeast-3.amazonaws.com/20250912-el2nl-voice-conversion/el2nl/{name}/audio/jvs001/{idx}.wav?t={int(time.time())}"
    return url


if "samples" not in st.session_state:
    idcs = [
        "001",
        "011",
        "017",
        "021",
        "025",
        "035",
        "036",
        "058",
        "065",
        "071",
        "075",
        "077",
        "086",
        "088",
        "092",
    ]
    samples = []
    for idx in idcs:
        for name in ["qvc_ft_pair_flat_10k"]:
            samples.append(
                {
                    "url_a": get_url(idx, "qvc_ft_10k"),
                    "url_b": get_url(idx, name),
                    "model_name": name,
                    "idx": idx,
                    "swap": np.random.rand() > 0.5,
                }
            )
    np.random.shuffle(samples)
    st.session_state["samples"] = samples
if "num_samples" not in st.session_state:
    st.session_state["num_samples"] = len(st.session_state["samples"])
if "sample_idx" not in st.session_state:
    st.session_state["sample_idx"] = 0


def choice_to_value(choice: str) -> int:
    value = 0
    match choice:
        case "A":
            value = 2
        case "ややA":
            value = 1
        case "ややB":
            value = -1
        case "ややB":
            value = -2
    return value


def on_form_submitted():
    # Record choice
    pair = st.session_state["samples"][st.session_state["sample_idx"]]
    intonation_value = choice_to_value(
        st.session_state[f'intonation_choice_{st.session_state["sample_idx"]}']
    )
    intelligibility_value = choice_to_value(
        st.session_state[f'intelligibility_choice_{st.session_state["sample_idx"]}']
    )

    if pair["swap"]:
        intonation_value = -intonation_value
        intelligibility_value = -intelligibility_value

    st.session_state["samples"][st.session_state["sample_idx"]][
        "intonation"
    ] = intonation_value
    st.session_state["samples"][st.session_state["sample_idx"]][
        "intelligibility"
    ] = intelligibility_value

    # Move to next pair
    st.session_state["sample_idx"] += 1


# Interface
st.title("セクション１")
st.warning(
    "ページを更新したりタブを閉じたりしないでください。入力済みのデータが失われます。"
)
progress_bar_text = "進捗"
progress_bar = st.progress(
    0, text=f"{progress_bar_text}: {0}/{st.session_state['num_samples']}"
)


@st.fragment
def exp_fragment():
    # Check if all completed
    if st.session_state["sample_idx"] == st.session_state["num_samples"]:
        st.session_state["log"] = {"com": st.session_state["samples"]}
        # Clean
        del st.session_state["samples"]
        del st.session_state["sample_idx"]
        del st.session_state["num_samples"]
        for k in st.session_state.keys():
            if not isinstance(k, str):
                continue
            if k.startswith("intonation_choice") or k.startswith(
                "intelligibility_choice"
            ):
                del st.session_state[k]

        # Move to next
        st.switch_page("pages/exp_sim.py")

    # Get sample info
    sample = st.session_state["samples"][st.session_state["sample_idx"]]
    url_a = sample["url_a"]
    url_b = sample["url_b"]
    if sample["swap"]:
        url_a, url_b = url_b, url_a

    # Place interface
    with st.container(border=True):
        st.subheader("自然さ・明瞭性")
        st.text(f"音声を聞いて、質問にお答えください。")
        cols = st.columns(2, border=True)
        cols[0].text("音声A")
        cols[0].audio(url_a)
        cols[1].text("音声B")
        cols[1].audio(url_b)
        intonation_choice = st.radio(
            "Q1: **イントネーションの自然さ**について、どちらの方が自然に聞こえますか？",
            options=[
                "A",
                "ややA",
                "どちらとも言えない",
                "ややB",
                "B",
            ],
            index=None,
            key=f'intonation_choice_{st.session_state["sample_idx"]}',
            horizontal=True,
        )
        intelligibility_choice = st.radio(
            "Q2: **明瞭性**について，どちらの方が聞き取りやすいと感じますか?",
            options=[
                "A",
                "ややA",
                "どちらとも言えない",
                "ややB",
                "B",
            ],
            index=None,
            key=f'intelligibility_choice_{st.session_state["sample_idx"]}',
            horizontal=True,
        )
        choice_has_not_been_made = (
            intonation_choice == None or intelligibility_choice == None
        )
        st.button(
            "次へ",
            on_click=on_form_submitted,
            disabled=choice_has_not_been_made,
            help="質問にお答えください。" if choice_has_not_been_made else "",
        )

    progress_bar.progress(
        st.session_state["sample_idx"] / st.session_state["num_samples"],
        f"{progress_bar_text}: {st.session_state['sample_idx']}/{st.session_state['num_samples']}",
    )


exp_fragment()
