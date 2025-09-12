import streamlit as st

st.title("実験紹介")

with st.container(border=True):
    st.header("内容")
    st.text(
        "本実験では、5〜10秒程度の発話音声のペアを聞いていただき、その音声に関する質問にご回答ください。\n\n"
        "各音声ペアに、以下に関する質問が用意されています。\n"
        "(1) イントネーションの自然さ：イントネーションが、どちらの音声の方が自然に聞こえるかを評価してください。\n"
        "(2) 明瞭性：発話内容がどちらの音声の方が聞き取りやすいかを評価してください。\n\n"
        "各質問にはラジオボタン式の選択肢があります。\n"
        "音声ペアをAとBとした場合、ラジオボタンは以下の5個で構成されています。もっとも当てはまるものを選択してください。\n"
        "(1) A\n"
        "(2) ややA\n"
        "(3) 分からない\n"
        "(4) ややB\n"
        "(5) B\n\n"
        "どちらも同じくらい良い、もしくはどちらも同じくらい良くない場合は、「(3) 分からない」を選んでください。\n\n"
        "音声は繰り返し聞くことが可能ですが、最大2回までとしてください。\n\n"
        "全部で20の音声ペアを聞いて評価していただきます。所要時間は15～20分程度です。"
    )

    st.header("インタフェース")
    st.text(
        "以下に、実際に使用していただくインターフェースの例を示します。\n\n"
        "- 音声を再生して、スピーカーの動作を事前に確認できます。\n\n"
        "- 画面が大きすぎる・小さすぎる場合は、ブラウザのズーム機能（Ctrl/CMD＋「+」「-」キー）で拡大・縮小してください。"
    )

    with st.container(border=True):
        st.subheader("音声を聞いていただき、質問にご回答ください。")
        columns = st.columns(2, border=True)
        columns[0].text("Audio A")
        columns[0].audio(
            "https://wu-cloud-bucket.s3.ap-northeast-3.amazonaws.com/202507-abnormal-voice-conversion/qvc/100.wav"
        )
        columns[1].text("Audio B")
        columns[1].audio(
            "https://wu-cloud-bucket.s3.ap-northeast-3.amazonaws.com/202507-abnormal-voice-conversion/qvc_enc_p_flow/100.wav"
        )
        st.radio(
            "Q1: イントネーションの自然さについて、どちらの方が自然に聞こえますか？",
            options=[
                "A",
                "ややA",
                "分からない",
                "ややB",
                "B",
            ],
            index=None,
            horizontal=True,
        )
        st.radio(
            "Q2: 明瞭性について、どちらの方が聞き取りやすいと感じますか？",
            options=[
                "A",
                "ややA",
                "分からない",
                "ややB",
                "B",
            ],
            index=None,
            horizontal=True,
        )

    st.warning(
        "音声を最後まで聞かず、ランダム的に回答されていると判断される場合は、報酬を支払えないことがあります。"
    )

next_button = st.button(label="実験へ")
if next_button:
    st.switch_page("pages/exp.py")
