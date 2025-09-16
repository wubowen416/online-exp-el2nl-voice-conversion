import time

import numpy as np
import streamlit as st

# np.random.seed(1234)


def get_url(idx: str, name: str, hid: str):
    url = f"https://wu-cloud-bucket.s3.ap-northeast-3.amazonaws.com/20250912-el2nl-voice-conversion/el2nl/{name}/audio/jvs{hid}/{idx}.wav?t={int(time.time())}"
    return url


if "samples" not in st.session_state:
    hids = [
        "001",
        "021",
        "041",
        "061",
        "081",
        "001",
        "021",
        "041",
        "061",
        "081",
        "001",
        "021",
        "041",
        "061",
        "081",
    ]
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
    for i, hid in enumerate(hids):
        if i < 5:
            samples.append(
                {
                    "url": get_url(idcs[i], "gt", hid),
                    "anchor_url": get_url("100", "gt", hid),
                    "model_name": "gt",
                    "hid": hid,
                    "idx": idcs[i],
                }
            )
        samples.append(
            {
                "url": get_url(idcs[i], "qvc_ft_10k", hid),
                "anchor_url": get_url("100", "gt", hid),
                "model_name": "qvc_ft_10k",
                "hid": hid,
                "idx": idcs[i],
            }
        )
    for sample in samples:
        print(sample["url"])
    np.random.shuffle(samples)
    st.session_state["samples"] = samples
if "num_samples" not in st.session_state:
    st.session_state["num_samples"] = len(st.session_state["samples"])
if "sample_idx" not in st.session_state:
    st.session_state["sample_idx"] = 0


def choice_to_value(choice: str) -> int:
    value = 3
    match choice:
        case "まったく似ていない":
            value = 1
        case "似ていない":
            value = 2
        case "似ている":
            value = 4
        case "とても似ている":
            value = 5
    return value


def on_form_submitted():
    # Record choice
    sim_value = choice_to_value(
        st.session_state[f'sim_choice_{st.session_state["sample_idx"]}']
    )
    st.session_state["samples"][st.session_state["sample_idx"]]["sim"] = sim_value

    # Move to next pair
    st.session_state["sample_idx"] += 1


# Interface
st.title("セクション２")
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
        st.session_state["log"]["sim"] = st.session_state["samples"]
        st.switch_page("pages/comment.py")

    # Get sample info
    sample = st.session_state["samples"][st.session_state["sample_idx"]]
    url = sample["url"]
    anchor_url = sample["anchor_url"]

    # Place interface
    with st.container(border=True):
        st.subheader("声の類似度（イントネーションや明瞭度は無視）")
        st.text(f"音声を聞いて、質問にお答えください。")
        cols = st.columns(2, border=True)
        cols[0].text("音声A")
        cols[0].audio(url)
        cols[1].text("音声B")
        cols[1].audio(anchor_url)
        sim_choice = st.radio(
            "**声の類似度**について、音質を無視して、音質音声AとBの声は似ていると思いますか",
            options=[
                "とても似ている",
                "似ている",
                "どちらとも言えない",
                "似ていない",
                "まったく似ていない",
            ],
            index=None,
            key=f'sim_choice_{st.session_state["sample_idx"]}',
        )
        choice_has_not_been_made = sim_choice is None
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
